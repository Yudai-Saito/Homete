import Vue from 'vue'
import VueRouter from 'vue-router'
import Top from '../views/Top.vue'

Vue.use(VueRouter)

const routes = [
	{
		path: '/',
		name: 'Top',
		component: Top,
		meta: {title: 'トップ'}
	},
	{
		path: '/about',
		name: 'About',
		// route level code-splitting
		// this generates a separate chunk (about.[hash].js) for this route
		// which is lazy-loaded when the route is visited.
		component: () => import(/* webpackChunkName: "about" */ '../views/About.vue'),
		meta: {title: 'HOMETEとは？'}
	},
	{
		path: '/login',
		name: 'Login',
		component: () => import('../views/Login.vue'),
		meta: {title: 'ログイン'}
	},
	{
		path: '/signup',
		name: 'Signup',
		component: () => import('../views/Signup.vue'),
		meta: {title: '新規登録'}
	},
	{
		path: '/signup/mail',
		name: 'SignupReqmail',
		component: () => import('../views/SignupReqmail.vue'),
		meta: {title: '新規登録'}
	},
	{
		path: '/passreset',
		name: 'Passreset',
		component: () => import('../views/Passreset.vue'),
		meta : {title: 'パスワード再設定'}
	},
	{
		path: '/passreset/mail',
		name: 'PassresetReqmail',
		component: () => import('../views/PassresetReqmail.vue'),
		meta : {title: 'パスワード再設定用'}
	},
]

const router = new VueRouter({
	mode: 'history',
	base: process.env.BASE_URL,
	routes,
    scrollBehavior () {
		return { x: 0, y: 0 }
	}
})

export default router
