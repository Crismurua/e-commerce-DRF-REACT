import React from 'react';
import s from './styles/Footer.module.css';
import { AiOutlineMail } from 'react-icons/ai';
import { TiSocialTwitter, TiSocialInstagram, TiSocialYoutube, TiSocialFacebook } from 'react-icons/ti';
export interface FooterProps {}

const Footer : React.FC<FooterProps> = () => {
	return (
		<>
		<footer>
			<div className={s.contact}>
				<h2><strong>KEEP IN TOUCH!</strong></h2>
				<form action="submit">
					<input type="text" placeholder='Sign up for Emails' />
					<button type='submit'><AiOutlineMail /></button>
				</form>
			</div>

			<div className={s.links}>
				<ul>
					<li>Help Center</li>
					<li>Product Help</li>
					<li>Order Status</li>
					<li>Custom Products</li>
					<li>Payment Policy</li>
					<li>Recycling</li>
					<li>Releases</li>
					<li>About</li>
					<li>Careers</li>
					<li>Contact Us</li>
				</ul>
			</div>

			<div className={s.social}>
				<h2><strong>FOLLOW US</strong></h2>
				<div>
					<i>
						<TiSocialTwitter size={40}/>
					</i>
					<i>
						<TiSocialInstagram size={40}/>
					</i>
					<i>
						<TiSocialYoutube size={40}/>
					</i>
					<i>
						<TiSocialFacebook size={40}/>
					</i>
				</div>
			</div>
		</footer>
		<div className={s.extra}>
				<div>Privacy Policy | Terms of Use | Consumer Rights</div>
				<div>© 2023 Raven Store All Rights Reserved</div>
				<div><img src="creditcardlogos1.webp" alt="payment" /></div>
		</div>
		</>
	)
};

export default Footer;
