import React, { useState } from 'react';
import LeafletMap from './LeafletMap';
import './App.css';

function App() {
  const [selectedDate, setSelectedDate] = useState(new Date());
  const [buttonClicked, setButtonClicked] = useState(false);
  const [dataToConsole, setDataToConsole] = useState(null); // Добавьте состояние для данных

   const handleDateChange = (event) => {
    const newDate = new Date(event.target.value);
    setSelectedDate(newDate);
  };

  const handleButtonClick = () => {
    setButtonClicked(true);
    
    const formattedJson = JSON.stringify(dataToConsole, null, 2);
    
    // Форматирование с отступами
    console.log(formattedJson);
  };
  

  const minDate = new Date().toISOString().split('T')[0];

  return (
    <div className='centralDiv'>
      <div className="container">
        <input
          className="date-input"
          type="date"
          value={selectedDate.toISOString().split('T')[0]}
          min={minDate}
          onChange={handleDateChange}
        />
      </div>
      <div>
        <LeafletMap
          selectedDate={selectedDate}
          buttonClicked={buttonClicked}
          setDataToConsole={setDataToConsole} // Передайте функцию для установки данных
        />
      </div>
      <div className='containerSend'>
        <button className='sendBtn' onClick={handleButtonClick}>Submit</button>
      </div>
    
    </div>
  );
}

export default App;
