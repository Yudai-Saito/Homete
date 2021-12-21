import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
	{
		path: '/',
		name: 'Home',
		component: Home
	},
	{
		path: '/About',
		name: 'About',
		// route level code-splitting
		// this generates a separate chunk (about.[hash].js) for this route
		// which is lazy-loaded when the route is visited.
		component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
	},
	{
		path: '/Login',
		name: 'Login',
		component: () => import('../views/Login.vue')
	},
	{
		path: '/Signup',
		name: 'Signup',
		component: () => import('../views/Signup.vue')
	},
	{
		path: '/SignupReqmail',
		name: 'SignupReqmail',
		component: () => import('../views/SignupReqmail.vue')
	},
	{
		path: '/Passreset',
		name: 'Passreset',
		component: () => import('../views/Passreset.vue')
	},
	{
		path: '/PassresetReqmail',
		name: 'PassresetReqmail',
		component: () => import('../views/PassresetReqmail.vue')
	},
]

const router = new VueRouter({
	mode: 'history',
	base: process.env.BASE_URL,
	routes
})

export default router
