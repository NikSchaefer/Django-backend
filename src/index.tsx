import React from 'react';
import ReactDOM from 'react-dom';
import './App.css';
import { useState } from 'react';

let content: number[] = [];

function Render(props: { arr: number[] }): any {
  let out: any[] = [];
  for (let i: number = 0; i < props.arr.length; i++) {
    out.push(
      <div className='inside' style={{ height: props.arr[i] * 8 }}></div>
    )
  }
  return out
}
function App() {


  const [con, setContent] = useState<any>([])

  window.onload = function () {
    for (let j = 0; j < 50; j++) {
      content.push(j)
      setContent([...con, 8])
    }
  }

  return (
    <div className='home'>
      <div className='content-div'>
        <Render arr={content} />
      </div>

    </div>
  );
}
ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);