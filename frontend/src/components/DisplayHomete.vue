<template>
	<v-container fluid>
		<v-card
			outlined
		>
			<h4 class="ml-4 mt-2">匿名さん</h4>
			<v-divider class="mx-4"></v-divider>
			<v-card-text>
				{{homete}}
			</v-card-text>
			<v-card-actions>
					<ReactionButton
						v-for="reaction in reactions"
						:key="reaction"
						:reactionIcon=reaction
					/>
			</v-card-actions>
		</v-card>
	</v-container>
</template>

<script>
import ReactionButton from '../components/ReactionButton'
export default{
	name: 'DisplayHomete',
	data(){
		return{
			homete: 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore',
			reactions:{
				good: '👍',
				interesting: '👀',
				great: '💯',
				like: '🥰',
				congratulations: '🎉',
			},
		}
	},
	components:{
		ReactionButton,
	},
	methods: {
		
	},
}
</script>