import './App.css';
import Dados from './components/Dados';


function App() {

  const nome='Eduardo Araujo'
  const idade='34 years'
  const cargo='Gerente de Redes e Multiserviços'
  
  return (
  <>
    <Dados nome={nome} idade={idade} cargo={cargo} />
  </>
  )
}

export default App;
