import styles from './index.less';
import Neuron from '@/components/Neuron';
import ReactFlow from 'react-flow-renderer';
import { useState } from 'react';


export default function IndexPage() {
  const [ elements, setElements ] = useState<Array<any>>([]);
  const [ x, setX ] = useState<number>(0);



  setInterval(() => {
    setX(x+1);
  }, 1000)

  return (
    <div className={styles.container}>
      <ReactFlow elements={[ { id: '1', data: { label: x }, position: { x: 250, y: 5 } },
      { id: '2', data: { label: 8 }, position: { x: 100, y: 100 } },
      { id: '3', data: { label: 9 }, position: { x: 200, y: 100 } },
      { id: 'e1-2', source: '1', target: '2', animated: true },
      { id: 'e1-2', source: '3', target: '2', animated: true }
    ]} />
    </div>
  );
}
