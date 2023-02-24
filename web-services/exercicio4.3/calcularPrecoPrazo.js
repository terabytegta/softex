const { calcularPrecoPrazo } = require('correios-brasil');

let args = {
  // Não se preocupe com a formatação dos valores de entrada do cep, qualquer uma será válida (ex: 21770-200, 21770 200, 21asa!770@###200 e etc),
  sCepOrigem: '07000001',
  sCepDestino: '55641390',
  nVlPeso: '2',
  nCdFormato: '1',
  nVlComprimento: '20',
  nVlAltura: '50',
  nVlLargura: '40',
  nCdServico: ['04014', '04510'], //Array com os códigos de serviço
  nVlDiametro: '0',
};

calcularPrecoPrazo(args).then(response => {
  console.log(response);
});