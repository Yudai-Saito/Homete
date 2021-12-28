<template>
	<v-container fluid class="hometeCard">
		<v-card
			:loading="loading"
			:disabled="form || loading"
			outlined
			class="hometeCard"
		>
			<v-btn
				icon
				plain
				@click="closeCard"
				class="my-1 ml-1"
			>
				<v-icon
					color="black"
				>
					mdi-close
				</v-icon>
			</v-btn>
			<template slot="progress">
				<v-progress-linear
					color="deep-purple"
					height="10"
					indeterminate
				></v-progress-linear>
			</template>
			<v-form
				ref="form"
			>
				<v-btn
					icon
					plain
					@click="clearText"
					class="float-right mt-2 mr-2"
					v-show="clearVisible"
				>
					<v-icon
						small
						color="glay"
					>
						mdi-close-circle
					</v-icon>
				</v-btn>
				<v-textarea
					label="なにを褒めてもらう？"
					solo
					flat
					auto-grow
					rows="3"
					v-model="homete"
					@input="inputText"
				></v-textarea>
				<v-divider class="mx-4"></v-divider>
				<v-card-actions>
						<v-btn
							class="info ml-auto"
							@click="submit"
							elevation='0'
							rounded
						>
								投稿する
						</v-btn>
				</v-card-actions>
			</v-form>
		</v-card>
	</v-container>
</template>
<style>
	.hometeCard{
		position: sticky;
		width: 500px;
		bottom: 200px;
	}
</style>

<script>
export default{
	name: 'PostHomete',
	data(){
		return{
			form: false,
			loading: false,
			homete: '',
			clearVisible: false,
			overlay: false,
		}
	},
	methods: {
		submit: function() {
			this.loading = true
			setTimeout(() => {
				this.formReset()
				this.loading = false
			}, 1500)
		},
		formReset () {
			this.$refs.form.reset()
			this.params = { homete: ''}
		},
		inputText: function(){
			if(this.clearVisible == false){
				this.clearVisible = true
			}
			else if(this.homete == ''){
				this.clearVisible = false
			}
		},
		clearText: function(){
			this.homete = ''
			this.clearVisible = false
		},
		closeCard: function(){
			this.$emit('overlay',this.overlay)
		}
	},
}
</script>