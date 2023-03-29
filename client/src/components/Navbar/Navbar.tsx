import React from 'react';
import s from './styles/Navbar.module.css';
export interface NavbarProps {}

const Navbar : React.FC<NavbarProps> = () => {
	return <div className={s.navbar}>Navbar</div >;
};

export default Navbar;
