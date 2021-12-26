<template>
	<v-app>
		<v-navigation-drawer app>Navigation Lists</v-navigation-drawer>
		<PostHomete v-on:cardVisible='noticeVisible' v-if="cardVisible"/>
		<DisplayHomete />
	</v-app>
</template>

<script>
import PostHomete from '../components/PostHomete'
import DisplayHomete from '../components/DisplayHomete'
export default {
	name: "Home",
	data(){
		return{
			cardVisible: true,
		}
	},
	components: {
		PostHomete,
		DisplayHomete,
	},
	methods: {
		noticeVisible: function(childCardVisible){
			this.cardVisible = childCardVisible
			console.log(this.cardVisible)
		}
	},
};
</script>
