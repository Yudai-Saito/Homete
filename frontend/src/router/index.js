import Vue from 'vue'
import VueRouter from 'vue-router'
import Top from '../views/Top.vue'

Vue.use(VueRouter)

const routes = [
	{
		path: '/',
		name: 'Top',
		component: Top
	},
	{
		path: '/about',
		name: 'About',
		// route level code-splitting
		// this generates a separate chunk (about.[hash].js) for this route
		// which is lazy-loaded when the route is visited.
		component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
	},
	{
		path: '/login',
		name: 'Login',
		component: () => import('../views/Login.vue')
	},
	{
		path: '/signup',
		name: 'Signup',
		component: () => import('../views/Signup.vue')
	},
	{
		path: '/signup/mail',
		name: 'SignupReqmail',
		component: () => import('../views/SignupReqmail.vue')
	},
	{
		path: '/passreset',
		name: 'Passreset',
		component: () => import('../views/Passreset.vue')
	},
	{
		path: '/passreset/mail',
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
