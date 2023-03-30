import React from 'react';
import s from './styles/Home.module.css';
export interface HomeProps {}

const Home : React.FC<HomeProps> = () => {
	return (
	<div className={s.home}>

		<div className={s.flyer}>
			<img className={s.camera} src="media/camera.jpg" alt="photography" />
			<img className={s.gaming} src="media/gaming-banner.jpg" alt="gaming" />
			<img className={s.music} src="media/headphones.jpg" alt="headphones" />
		</div>
		
	</div >
	);
};

export default Home;
