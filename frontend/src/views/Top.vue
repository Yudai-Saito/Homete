<template>
	<v-app>
		<v-overlay
			:value="overlay"
			dark=false
			light=true
			:z-index="999"
		>
			<PostHomete
				v-on:overlay='noticeVisible'
				v-on:postAlert='alertPostVisible'
			/>
		</v-overlay>
		<v-container fluid class="mainContainer mx-auto">
			<v-expand-transition>
				<v-alert
					v-show="alertPost"
					color="primary"
					text
					type="success"
					class="alertSucess"
				>
					投稿しました!
				</v-alert>
			</v-expand-transition>
			<v-expand-transition>
				<v-alert
					v-show="alertLogin"
					color="green lighten-2"
					text
					type="success"
					class="alertSucess"
				>
					おかえりなさい
				</v-alert>
			</v-expand-transition>
			<v-expand-transition>
				<v-alert
					v-show="alertLogout"
					color="red accent-2"
					text
					type="success"
					class="alertSucess"
				>
					ログアウトが完了しました
				</v-alert>
			</v-expand-transition>
			<v-row justify="center" class="mx-auto">
				<v-col
					cols="2"
					class="d-none d-sm-block ma-0 pa-0 leftMenu"
				>
					<SideMenu
						class="leftMenuContent"
						v-on:overlay='overlayCard'
						v-on:logout="distinctLoginCheck"
						v-if="distinctLogin"
					/>
					<NoLoginSideMenu
						class="leftMenuContent"
						v-else
					/>
				</v-col>

				<v-app-bar
					elevation=0
					color=rgba(255,255,255,0.9)
					dense
					app
					class="topMenu"
					v-if="this.$vuetify.breakpoint.width < 500"
				>
					<v-app-bar-nav-icon
						@click="drawer = true"
						x-large
						class="navButton"
					></v-app-bar-nav-icon>

					<v-btn
						elevation=3
						fab
						color="white"
						icon
						class="postButton"
						@click="overlay = true"
					>
						<v-icon>
							mdi-pen-plus
						</v-icon>
					</v-btn>
				</v-app-bar>
				<v-navigation-drawer
					v-model="drawer"
					app
					touchless
					v-bind:width="150"
					v-if="this.$vuetify.breakpoint.width < 500"

				>
					<SideMenu
						class="leftMenuContent"
						v-on:overlay='overlayCard'
						v-on:logout="distinctLoginCheck"
						v-if="distinctLogin"
					/>
					<NoLoginSideMenu
						class="leftMenuContent"
						v-else
					/>
				</v-navigation-drawer>

				<v-divider vertical class="d-none d-sm-block"></v-divider>

				<v-col
					cols="12"
					sm="8"
					md="8"
					class="subContainer virtualScrollBar"
					v-scroll="onScroll"
				>
					<DisplayHomete 
						v-for="post in posts"
						:key="post"
						:postList=post
						:distinctLogin="distinctLogin"
					/>
				</v-col>

				<v-divider vertical class="d-none d-sm-block"></v-divider>
        
				<v-col md="2" class="hidden-sm-and-down ma-0 pa-0 mt-auto mr-1 rightMenu">
					
				</v-col>
			</v-row>
		</v-container>
	</v-app>
</template>
<style>
	.testColorA{
		background-color: cyan;
	}
	.testColorB{
		background-color: burlywood;
	}
	.mainContainer{
		max-width: 1200px;
		width: 100%;
		height: 100%;
	}
	.subContainer{
		width: 100%;
	}
	.leftMenu{
		width: 115pt;
		min-width: 115pt;
		max-width: 115pt;
		flex: none;
	}
	.leftMenuContent{
		position: sticky;
		top: 0px;
	}
	.rightMenu{
		min-width: 115pt;
	}
	.topMenu{
		width: 100vw;
		min-width: 100vw;
		max-width: 100vw;
		flex: none;
		margin: 0;
		padding: 0;
	}
	.postButton{
		position: absolute;
		margin-top: 170vh;
		margin-left: 75vw;
		background-color: #1DA1F2;
	}
	.navButton{
		margin-right: auto;
		margin-top: auto;
		margin-bottom: auto;
	}
	.virtualScrollBar{
		overflow: auto;
		/* IE, Edge 対応 */
		-ms-overflow-style: none;
		/* Firefox 対応 */
		scrollbar-width: none;
	}
	/* Chrome, Safari 対応 */
	.virtualScrollBar::-webkit-scrollbar {
		display:none;
	}
	.alertSucess{
		width: 90%;
		margin-right: auto;
		margin-left: auto;
	}
</style>


<script>
import PostHomete from '../components/PostHomete'
import DisplayHomete from '../components/DisplayHomete'
import SideMenu  from '../components/SideMenu'
import NoLoginSideMenu from '../components/NoLoginSideMenu.vue'
import axios from 'axios'


export default {
	name: "Top",
	data(){
		return{
			overlay: false,
			drawer: false,
			alertPost: false,
			alertLogin: false,
			alertLogout: false,
			alert: false,
			distinctLogin: false,
			posts:[],
			scrolledBottom: false,
	}
	},
	components: {
		PostHomete,
		DisplayHomete,
		SideMenu,
		NoLoginSideMenu,
	},
	methods: {
		noticeVisible: function(childOverlay){
			this.overlay = childOverlay
		},
		overlayCard: function(childOverlay){
			this.overlay = childOverlay
			this.drawer = false
		},
		alertPostVisible: function(childrenAlert){
			this.alertPost = childrenAlert
			setTimeout(() => {
				this.alertPost = false}
				,3000
			)
		},
		distinctLoginCheck: function(){
			this.distinctLogin = false
			localStorage.clear('firstLogin')
			setTimeout(() => {
				this.alertLogout = true}
				,500
			)
			setTimeout(() => {
				this.alertLogout = false}
				,3000
			)
		},
		onScroll: function(event) {
			if (this.isFullScrolled(event)) {
				// 一番下までスクロールした際の処理
				if(this.scrolledBottom == false){
					this.scrolledBottom = true

					//最終投稿の投稿時間をパラメーターに投稿取得APIを叩く
					axios.get('/post', {
							params:{
								created_at: this.posts[this.posts.length -1].created_at
							}
						},{
							withCredentials: true
						}
					).then((res) => {
						//投稿の追記
						this.posts = this.posts.concat(res.data)
						this.scrolledBottom = false
					}).catch((err) => {
						console.log(err)
					})
				}
			}
		},
		isFullScrolled(event){
			const adjustmentValue = (event.target.scrollingElement.clientHeight * 1.5)
			const positionWithAdjustmentValue = event.target.scrollingElement.clientHeight + event.target.scrollingElement.scrollTop + adjustmentValue
			return positionWithAdjustmentValue >= event.target.scrollingElement.scrollHeight
		}
	},
	created(){
		if(this.$cookies.isKey("expire") == true){
			this.distinctLogin = true
			if(!localStorage.getItem('firstLogin')){
				setTimeout(() => {
					this.alertLogin = true}
					,1500
				)
				setTimeout(() => {
					this.alertLogin = false}
					,3000
				)
			}
			localStorage.setItem('firstLogin',true)
		}
		else{
			this.distinctLogin = false
		}

		axios.get('/post',{
				withCredentials: true
			}
		).then((res) => {
			this.posts = res.data
		}).catch((err) => {
			console.log(err)
			}
		)
	}
};
</script>