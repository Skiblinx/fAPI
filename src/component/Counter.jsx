import { useState, useEffect } from 'react';
import { ChevronUp, ChevronsUp, ChevronDown, Hash, RotateCcw, ChevronsDown } from 'react-feather';


function Counter() {
  const [count, setCount] = useState(0);

  
  useEffect(() => {
 
    document.title = `Count: ${count}`;
  }, [count]);

  const countStyle = {
    color: count < 0 ? 'red' : count === 0 ? 'blue' : 'green',
  };

  const handleIncrement = (value) => {
    setCount((prev) => prev + value);
  };

  const handleReset = () => {
    setCount(0);
  };

  const handleRandomize = () => {
    setCount(Math.trunc(Math.random() * 100) + 1);
  };

  return (
    <div className='counter-card'>
      <p>Current value</p>
      <h1 style={countStyle}>{count}</h1>
      <div className='card'>
        <button onClick={() => handleIncrement(1)}>
          <ChevronUp />
        </button>
        <button onClick={() => handleIncrement(10)}>
          <ChevronsUp />
        </button>
        <button onClick={handleReset}>
          <RotateCcw />
        </button>
        <button onClick={handleRandomize}>
          <Hash />
        </button>
        <button onClick={() => handleIncrement(-10)}>
          <ChevronsDown />
        </button>
        <button onClick={() => handleIncrement(-1)}>
          <ChevronDown />
        </button>
      </div>
    </div>
  );
}


export default Counter;