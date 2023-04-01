import React, {useState, useEffect} from 'react';
import { useNavigate } from 'react-router-dom';
import s from './styles/Navbar.module.css';
import { FaUserCircle } from 'react-icons/fa';
import { AiOutlineShoppingCart, AiOutlineSearch } from 'react-icons/ai';

export interface NavbarProps {}

const Navbar : React.FC<NavbarProps> = () => {

	const [isLogoVisible, setIsLogoVisible] = useState(true);
	const navigate = useNavigate();

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
				<div className={s.img} onClick={()=>navigate('/')}>
					<img className={s.imglogo} src="2.png" alt="logo" />
					<h2 className={`${s.textlogo} ${isLogoVisible ? s.visible : s.hidden}`}>Raven Store</h2>
				</div>
				<ul>
					<li className={s.dropdown}>
						<button className={s.button}>SHOP</button>
						<ul className={s.submenu}>
							<h3>Categories</h3>
      					  <li>Category 1</li>
      					  <li>Category 2</li>
      					  <li>Category 3</li>
      					  <li>Category 1</li>
      					  <li>Category 2</li>
      					  <li>Category 3</li>
      					  <li>Category 1</li>
      					  <li>Category 2</li>
      					  <li>Category 3</li>
      					</ul>
					</li>
					<li>
						<button className={s.button}>ABOUT</button>
					</li>
				</ul>
			</div>
			<div className={s.buttons}>
				<span>
					<AiOutlineSearch />
				</span>
				<span>
					<FaUserCircle onClick={()=>navigate('login')}/>
				</span>
				<span>
					<AiOutlineShoppingCart />
				</span>
			</div>
		</div >
		<p className={s.info}>info about free shipping and promotions</p>
		</>
	)
};

export default Navbar;
