open Printf
open Scanf

let abs x = if (x > 0) then x else -x;;

let () =
  let n = (Scanf.scanf "%d\n" (fun x -> x - 1)) in
      for i=0 to 2*n do
        let m = n - abs(i-n) in
          for j=1 to m do
            printf(" ")
          done;
          for j=0 to 2*n - 2*m do
            printf("*")
          done;
          printf("\n");
      done;;
