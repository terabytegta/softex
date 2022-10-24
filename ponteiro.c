int main(void)
{
  float *ponteiro; 
  int i, tam, inc, op, num;
  tam = 22;
  ponteiro = (float *) malloc(tam * sizeof(float));
  
  for (i = 0; i < tam; i++)
  {
    printf("\nInsira um valor para a posição do vetor: ", i+1);
    scanf("%f",&ponteiro[i]);
  }
  
  printf("\nDeseja incrementar algum número?: ");
  printf("\n1 - Sim");
  printf("\n2 - Não\n");
  scanf("%d", &op);

  if (op == 1)
  {
    printf("Quantos números você deseja incrementar?: ");
    scanf("%d", &num);
    
    inc = num + tam;

    ponteiro = (float *) realloc(ponteiro, inc * sizeof (float));
    for (i = i; i < inc; i++)
  {
    printf("\nInsira um valor para a posição do vetor: ", i+1);
    scanf("%f",&ponteiro[i]);
  }

  }
  else
  {
    inc = tam;
  }

  for (i = 0;i < inc; i++)
  {
    printf("%.2f\n",ponteiro[i]);
  }
  
  free(ponteiro);
  getch();
  return 0;
}
