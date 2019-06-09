<template>
	<div>
	  <section class="section">
	    <div class="container">
	      <a href="/"><h1 class="title is-1">Titanic Survival Predictor</h1></a>
	      <h3 class="subtitle is-3">Would you have survived disaster?</h3>
	      <hr>
	      <div class="message is-success" v-if="result > 60">
	        <div class="message-header">
	          <p>Results</p>
	        </div>
	        <div class="message-body">
	          <h1 class="title is-3">Chance of survival: {{result}}%</h1>
	          <h1 class="subtitle is-5">Congratz! {{name}}, It looks like you would survive this horrible disaster.</h1>
	        </div>
	      </div>
	      <div class="message is-warning" v-if="result >= 50 && result <= 60">
	        <div class="message-header">
	          <p>Results</p>
	        </div>
	        <div class="message-body">
	          <h1 class="title is-3">Chance of survival: {{result}}%</h1>
	          <h1 class="subtitle is-5">Oh... Well, {{name}}, try and hold your breath..</h1>
	        </div>
	      </div>
	      <div class="message is-danger" v-if="result < 50">
	        <div class="message-header">
	          <p>Results</p>
	        </div>
	        <div class="message-body">
	          <h1 class="title is-3">Chance of survival: {{result}}%</h1>
	          <h1 class="subtitle is-5">{{name}}, this is just sad... :(</h1>
	        </div>
	      </div>
	    </div>
	  </section>
  </div>
</template>

<script>
	export default {
		name: 'result',
		data() {
			return {
				result: this.$route.params.result,
				name: this.$route.params.name.split(" ")[0]
			}
		}
	}
</script>