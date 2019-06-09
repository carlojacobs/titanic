<template>
  <div class="home">
    <section class="section">
      <div class="container">
        <a href="/"><h1 class="title is-1">Titanic Survival Predictor</h1></a>
        <h3 class="subtitle is-3">Would you have survived disaster?</h3>
        <hr>
        <div class="columns">
          <div class="column">
            <h4 class="title is-4">Fill in this form and find out!</h4>
            <form>
              <div class="field">
                <label class="label">Name</label>
                <div class="control">
                  <input class="input" type="text" :class="{'is-danger': nameInvalid}" placeholder="Name" name="name" v-model="name">
                </div>
                <p class="help is-danger" v-if="nameInvalid">Please fill in this field</p>
              </div>
              <div class="field">
                <label class="label">Age</label>
                <div class="control">
                  <input class="input" :class="{'is-danger': ageInvalid}" type="number" placeholder="Age" name="age" v-model="age">
                </div>
                <p class="help is-danger" v-if="ageInvalid">Please fill in this field</p>
              </div>
              <div class="field">
                <label class="label">Gender</label>
                <div class="control">
                  <label class="radio">
                    <input type="radio" name="gender" value="0" checked v-model="gender">
                    Male
                  </label>
                  <label class="radio">
                    <input type="radio" name="gender" value="1" v-model="gender">
                    Female
                  </label>
                  <p class="help is-danger" v-if="genderInvalid">Please fill in this field</p>
                </div>
              </div>
              <div class="field">
                <label class="label">Number of Siblings on Board</label>
                <div class="control">
                  <input class="input" :class="{'is-danger': sibsInvalid}" type="number" placeholder="Number of Siblings" name="sibs" v-model="sibs">
                  <p class="help is-danger" v-if="sibsInvalid">Please fill in this field</p>
                </div>
              </div>
              <div class="field">
                <label class="label">Number of Parents on Board</label>
                <div class="control">
                  <input class="input" :class="{'is-danger': parsInvalid}" type="number" placeholder="Number of Parents" name=pars v-model="pars">
                  <p class="help is-danger" v-if="parsInvalid">Please fill in this field</p>
                </div>
              </div>
              <div class="field">
                <label class="label">Ebarked from Port</label>
                <div class="control">
                  <div class="select" :class="{'is-danger': embarkedInvalid}">
                    <select name="embarked" v-model="embarked">
                      <option value="0">Cherbourg</option>
                      <option value="1">Southampton</option>
                      <option value="2">Queenstown</option>
                    </select>
                  </div>
                  <p class="help is-danger" v-if="embarkedInvalid">Please fill in this field</p>
                </div>
              </div>
              <div class="field">
                <label class="label">Class</label>
                <div class="control" :class="{'is-danger': classInvalid}">
                  <label class="radio">
                    <input type="radio" name="class" value="1" checked v-model="pclass">
                    1st
                  </label>
                  <label class="radio">
                    <input type="radio" name="class" value="2" v-model="pclass">
                    2nd
                  </label>
                  <label class="radio">
                    <input type="radio" name="class" value="3" v-model="pclass">
                    3rd
                  </label>
                  <p class="help is-danger" v-if="classInvalid">Please fill in this field</p>
                </div>
              </div>
              <div class="field">
                <div class="control">
                  <button type="button" class="button is-link" v-on:click="predict()">Submit</button>
                </div>
              </div>
            </form>
          </div>
          <div class="column">
            <h4 class="title is-4">What Happened?</h4>
            <div class="content">
              <p>RMS Titanic was a British passenger liner that sank in the North Atlantic Ocean in 1912, after colliding with an iceberg during her maiden voyage from Southampton to New York City. Of the estimated 2,224 passengers and crew aboard, more than 1,500 died, making it one of modern history's deadliest commercial marine disasters during peacetime. RMS Titanic was the largest ship afloat at the time she entered service and was the second of three Olympic-class ocean liners operated by the White Star Line. She was built by the Harland and Wolff shipyard in Belfast. Thomas Andrews, chief naval architect of the shipyard at the time, died in the disaster</p>
              <a href="https://en.wikipedia.org/wiki/Sinking_of_the_RMS_Titanic" class="button is-info">More</a>
              <br>
              <iframe src="https://giphy.com/embed/qXAkeaeRMPt16" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
            </div>
          </div>
        </div>
      </div>
    </section>
    <footer class="footer">
      <div class="content has-text-centered">
        <p>
          <strong>Titanic Predictor</strong> by <a href="https:carlo-jacobs.com">Carlo Jacobs</a>. The source code is licensed
          <a href="http://opensource.org/licenses/mit-license.php">MIT</a>.
        </p>
      </div>
    </footer>
  </div>
</template>

<script>
// Import tensorflow js
import * as tf from '@tensorflow/tfjs';

let model;
(async function() {
  model = await tf.loadLayersModel('http://carlo-jacobs.com/titanic/94_js_model/model.json');
})();

/*
name: "",
  		age: "",
  		gender: "",
  		sibs: "",
  		pars: "",
  		embarked: "",
  		pclass: "",

  		*/

export default {
  name: 'home',
  data() {
  	return {
  		name: "",
  		age: "",
  		gender: "",
  		sibs: "",
  		pars: "",
  		embarked: "",
  		pclass: "",
  		nameInvalid: false,
  		ageInvalid: false,
  		genderInvalid: false,
  		sibsInvalid: false,
  		parsInvalid: false,
  		embarkedInvalid: false,
  		classInvalid: false,
  	}
  },
  methods: {
  	validate() {
  		this.nameInvalid = (this.name == "");
  		this.ageInvalid = (this.age == "");
  		this.genderInvalid = (this.gender == "");
  		this.sibsInvalid = (this.sibs == "");
  		this.parsInvalid = (this.pars == "");
  		this.classInvalid = (this.pclass == "");
  		this.embarkedInvalid = (this.embarked == "");
  		if (!this.nameInvalid && !this.genderInvalid && !this.ageInvalid && !this.sibsInvalid && !this.parsInvalid && !this.classInvalid && !this.embarkedInvalid) {
  			return true;
  		} else {
  			return false;
  		}
  	},
  	predict() {
  		if (this.validate()) {
  			/*
					Final order of data:
					class,
					gender,
					age,
					sibs,
					pars,
					ticket,
					embarked
				*/

				// Get ticket price
				let ticket;
				if (this.pclass == 1) {
					ticket = 60;
				} else if (this.pclass == 2) {
					ticket = 40;
				} else if (this.pclass == 3) {
					ticket = 7;
				}

				const pclass = Number(this.pclass);
				const gender = Number(this.gender);
				const age = Number(this.age);
				const sibs = Number(this.sibs);
				const pars = Number(this.pars);
				const embarked = Number(this.embarked);
        const name = this.name;


				var data = [pclass, gender, age, sibs, pars, ticket, embarked];
				const prediction = model.predict(tf.tensor([data]));
				prediction.data().then(data => {
					const result = Math.round(data[0] * 100);
          this.$router.push('/result/' + result + '/' + name);
				});
  		}
  	}
  }
}
</script>
