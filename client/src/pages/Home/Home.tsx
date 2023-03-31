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
		<section className={s.gallery}>
			<h2>Trends</h2>
			<div>
				<div>Product 1</div>
				<div>Product 2</div>
				<div>Product 3</div>
			</div>

		</section>

		<article className={s.sale}>
			<img src="media/blackfriday.png" alt="blackfriday" />
		</article>
	</div >
	);
};

export default Home;
