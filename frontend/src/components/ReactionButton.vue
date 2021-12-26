<template>
	<v-btn
		class="justify-start"
		@click="countup"
		elevation='0'
		small
	>
		<h2>{{reactionIcon}}</h2>{{reactionCount}}
	</v-btn>
</template>

<script>
export default{
	name: 'ReactionButton',
	data(){
		return{
			reactionCount: 0,
		}
	},
	props:[
		'reactionIcon'
	],
	methods: {
		countup: function(){
			this.reactionCount += 1
		}
	},
}
</script>