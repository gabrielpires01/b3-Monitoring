import { Routes, Route } from 'react-router-dom';
import Home from './components/Home/Home';
import Quotation from './components/Home/Quotation';

function App() {
  return (
    <Routes>
      <Route path='' element={<Home />}/>
      <Route path='/quotations' element={<Quotation />}/>
    </Routes>
  );
}

export default App;