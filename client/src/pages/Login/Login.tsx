import React from 'react';
import s from './styles/Login.module.css';
export interface LoginProps {}

const Login : React.FC<LoginProps> = () => {
	return (
		<div className={s.login}>
			<section>
				<h2><strong>SIGN IN</strong></h2>
				<form>
					<div>
						<p>Email:</p>
						<input type="text"/>
					</div>
					<div>
						<p>Password:</p>
						<input type="text"/>
					</div>
					<button type='submit'>SIGN IN</button>
				</form>
				<button className={s.google}>Sign in with Google</button>
				<button className={s.facebook}>Sign in with Facebook</button>
				
			</section>
			<section>
				<h2><strong>SIGN UP</strong></h2>
				<h4>NEW CUSTOMER?</h4>
				<p>Create an account with us and you'll be able to:</p>
				<ul>
					<li>Check out your products</li>
					<li>Track your orders</li>
					<li>Access to the Big Deals</li>
					<li>Suscribe to the news</li>
				</ul>
				<button>CREATE ACCOUNT</button>
			</section>
		</div >
	)
};

export default Login;
