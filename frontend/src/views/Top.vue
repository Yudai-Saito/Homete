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
					送信しました
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
				<v-col cols="2" class="d-none d-sm-block ma-0 pa-0 leftMenu">
					<SideMenu
						v-on:overlay='overlayCard'
						v-on:logout="distinctLoginCheck"
						v-if="distinctLogin"
					/>
					<NoLoginSideMenu v-else />
				</v-col>

				<v-app-bar
					elevation=0
					color=rgba(255,255,255,0.9)
					dense
					app
					class="topMenu"
					v-if="this.$vuetify.breakpoint.width < 555"
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
					v-if="this.$vuetify.breakpoint.width < 555"

				>
					<SideMenu
						v-on:overlay='overlayCard'
						v-on:logout="distinctLoginCheck"
						v-if="distinctLogin"
					/>
					<NoLoginSideMenu v-else />
				</v-navigation-drawer>

				<v-divider vertical class="d-none d-sm-block"></v-divider>

				<v-col cols="12" sm="8" md="8" class="subContainer">
					<DisplayHomete 
						v-for="post in posts"
						:key="post"
						:postList=post
					/>
				</v-col>

				<v-divider vertical class="d-none d-sm-block"></v-divider>

				<v-col md="2" class="hidden-sm-and-down ma-0 pa-0 rightMenu">
					<h2 align="center">column</h2>
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

var posts = [{
				"post_id" : 1,
				"created_at": "2021-12-25T23:32:19",
				"post_content": "絵文字を選んだ!",
				"post_reaction" : [
					{
						"reaction" : "👍",
						"count" : "3"
					},
					{
						"reaction" : "👀",
						"count" : "5"
					}
				],
				"user_reaction" : ["👍", "👀"]
			},
			{
				"post_id" : 2,
				"created_at": "2021-12-25T23:32:19",
				"post_content": "トップ画面ができた!",
				"post_reaction" : [
					{
						"reaction" : "👍",
						"count" : "4"
					}
				],
				"user_reaction" : []
			},
		]

export default {
	name: "Top",
	data(){
		return{
			overlay: false,
			drawer: false,
			alertPost: false,
			alertLogin: false,
			alertLogout: false,
			posts:posts,
			distinctLogin: false,
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
	},
	mounted(){
	},
	created() {
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
	},
	updated() {
	},
	computed:{
	}
};
</script>