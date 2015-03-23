void matvec_doit(double* output, double* matrix, double *vector, int n)
{
  double val;
  int i,j;
  for (i=0; i<n; i++)
    {
      val = 0;
      for (j=0; j<n; j++)
        {
          val += matrix[i*n+j]*vector[j];
        }
      output[i] = val;
    }
}
