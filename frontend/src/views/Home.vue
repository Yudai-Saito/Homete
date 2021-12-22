<template>
	<v-app>
		<v-navigation-drawer app>Navigation Lists</v-navigation-drawer>
		<PostHomete />
	</v-app>
</template>

<script>
import PostHomete from '../components/PostHomete'
export default {
	name: "Home",
	components: {
		PostHomete,
	},
};
</script>
