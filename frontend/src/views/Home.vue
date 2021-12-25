<template>
	<v-app>
		<v-navigation-drawer app>Navigation Lists</v-navigation-drawer>
		<PostHomete v-on:cardVisible='noticeVisible' v-if="cardVisible"/>
	</v-app>
</template>

<script>
import PostHomete from '../components/PostHomete'
export default {
	name: "Home",
	data(){
		return{
			cardVisible: true,
		}
	},
	components: {
		PostHomete,
	},
	methods: {
		noticeVisible: function(childCardVisible){
			this.cardVisible = childCardVisible
			console.log(this.cardVisible)
		}
	},
};
</script>
