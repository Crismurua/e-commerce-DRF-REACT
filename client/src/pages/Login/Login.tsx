import React from 'react';
import s from './styles/Login.module.css';
export interface LoginProps {}

const Login : React.FC<LoginProps> = () => {
	return (
		<div className={s.login}>Login</div >
	)
};

export default Login;
