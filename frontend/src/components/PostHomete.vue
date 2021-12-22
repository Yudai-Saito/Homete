<template>
	<v-container fluid>
		<v-card
			:loading="loading"
			:disabled="form || loading"
			outlined
		>
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
				<v-textarea
					clearable
					solo
					flat
					auto-grow
					rows="3"
					label="なにを褒めてもらう？"
					v-model="homete"
				></v-textarea>
				<v-divider class="mx-4"></v-divider>
				<v-card-actions>
						<v-btn
							class="info ml-auto"
							@click="submit">
								投稿する
						</v-btn>
				</v-card-actions>
			</v-form>
		</v-card>
	</v-container>
</template>

<script>
export default{
	name: 'PostHomete',
	data(){
		return{
			form: false,
			loading: false,
			homete: '',
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
	},
}
</script>