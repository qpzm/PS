const lines = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
var i = 1;
while(i < lines.length) {
  var [dim, days, src] = splitAndParse(lines[i++]);
  const matrix = lines.slice(i, i+dim).map(l => splitAndParse(l));
  i += dim;

  // Criterion: An index starts from 0 to dim - 1
  var probs = [...Array(matrix.length)].map(x => 0);
  probs[src] = 1;

  const adj_list = create_adj_list(matrix);
  while(days-- > 0) {
    probs = markov(probs, adj_list);
  }

  i++; // skip the test length
  const tests = splitAndParse(lines[i++]);
  console.log(tests.map(x => probs[x]).join(' '));
}

function splitAndParse(line) {
  return line.trim().split(' ').map(e => parseInt(e))
}

function markov(probs, adj_list) {
  var new_probs = [...Array(adj_list.length)].map(_ => 0);

  for(var i=0; i<probs.length; i++) {
    const p = probs[i];
    if(p > 0 && adj_list[i].length > 0) {
      const unit = p / adj_list[i].length;

      adj_list[i].forEach(neighbor => {
        new_probs[neighbor] += unit;
      });
    }
  }

  return new_probs;
}

function create_adj_list(matrix) {
  var adj_list = []

  for(var i=0; i<matrix.length; i++) {
    var adj_row = [];
    for(var j=0; j<matrix[i].length; j++) {
      if(matrix[i][j])
        adj_row.push(j);
    }
    adj_list.push(adj_row);
  }

  return adj_list;
}
