import React, {useState, useEffect} from 'react';
import s from './styles/Navbar.module.css';
import { FaUserCircle } from 'react-icons/fa';
import { AiOutlineShoppingCart, AiOutlineSearch } from 'react-icons/ai';

export interface NavbarProps {}

const Navbar : React.FC<NavbarProps> = () => {

	const [isLogoVisible, setIsLogoVisible] = useState(true);

	useEffect(() => {
		const handleScroll = () => {
		  const currentScrollPos = window.pageYOffset;
		  if (currentScrollPos > 0 && isLogoVisible) {
			setIsLogoVisible(false);
		  } else if (currentScrollPos === 0 && !isLogoVisible) {
			setIsLogoVisible(true);
		  }
		};
	
		window.addEventListener('scroll', handleScroll);
		return () => {
		  window.removeEventListener('scroll', handleScroll);
		};
	  }, [isLogoVisible]);

	return (
		<>
		<div className={s.container}>			
			<div className={s.logo}>
				<div className={s.img}>
					<img className={s.imglogo} src="2.png" alt="logo" />
					<h2 className={`${s.textlogo} ${isLogoVisible ? s.visible : s.hidden}`}>Raven Store</h2>
				</div>
				<button className={s.button}>SHOP</button>
				<button className={s.button}>ABOUT</button>
			</div>
			<div className={s.buttons}>
				<AiOutlineSearch />
				<FaUserCircle />
				<AiOutlineShoppingCart />
			</div>
		</div >
		<p className={s.info}>info about free shipping and promotions</p>
		</>
	)
};

export default Navbar;
