n,i,j;
main(){
  scanf("%d", &n);
  for(;i<n;i++){
    for(j=0;j<i;j++) printf(" ");
    for(;j<2*n-1-i;j++) printf("*");
    puts("");
  }
}
