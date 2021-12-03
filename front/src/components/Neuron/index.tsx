import styles from './index.less';

export default function Neuron(props: {x: number, y: number}) {
  return (
    <div className={styles.neuron} style={{top: props.x, left: props.y}}>
    </div>
  );
}
