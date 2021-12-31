<template>
	<div class="btnDiv">
		<v-btn
			class="d-none d-sm-block reactBtnA"
			@click="countup"
			elevation='0'
			small
		>
			<h2>{{reactionIcon}}</h2>{{reactionCount}}
		</v-btn>

		<v-btn
			class="d-block d-sm-none reactBtnB"
			@click="countup"
			elevation='0'
			x-small
		>
			<h3>{{reactionIcon}}</h3>{{reactionCount}}
		</v-btn>
	</div>
</template>
<style>
	.btnDiv{
		margin: 0;
		padding: 0;
	}
	.reactBtnA{
		margin: 0;
		margin-right: 9px;
	}
	.reactBtnB{
		margin: 0;
		min-height: 22px;
		margin-right: 3px;
	}
</style>

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