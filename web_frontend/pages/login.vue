<template>
  <v-main>
    <v-container class="fill-height" fluid>
      <v-row align="center" justify="center">
        <v-col cols="12" sm="8" md="8">
          <v-card class="elevation-12">
            <v-window v-model="step">
              <v-window-item :value="1">
                <v-row>
                  <v-col cols="12" md="8">
                    <v-card-text class="mt-12">
                      <h1 class="text-center display-2">Sign In</h1>
                      <h4 class="text-center mt-4">
                        Ensure your email for check in
                      </h4>
                      <v-form>
                        <v-text-field
                          v-model="username"
                          v-on:keyup.enter="signIn"
                          label="Name"
                          name="name"
                          prepend-icon="person"
                          type="text"
                          color="deep-purple accent-4"
                          required
                        />
                        <v-text-field
                          v-model="password"
                          v-on:keyup.enter="signIn"
                          id="password"
                          label="Password"
                          name="Password"
                          prepend-icon="lock"
                          type="password"
                          color="deep-purple accent-4"
                          required
                        />
                      </v-form>
                      <h3 class="text-center mt-3">Forget your password?</h3>
                    </v-card-text>
                    <div class="text-center mt-3">
                      <v-btn
                        rounded
                        color="deep-purple accent-4"
                        dark
                        @click="signIn"
                      >
                        SIGN IN
                      </v-btn>
                    </div>
                  </v-col>
                  <v-col cols="12" md="4" class="deep-purple accent-4">
                    <v-card-text class="white--text mt-12">
                      <h1 class="text-center display-1">Hello, Friend!</h1>
                      <h5 class="text-center">
                        Enter your personal details and start voting with us!
                      </h5>
                    </v-card-text>
                    <div class="text-center">
                      <v-btn rounded outlined dark @click="step++">
                        SIGN UP
                      </v-btn>
                    </div>
                  </v-col>
                </v-row>
              </v-window-item>
              <v-window-item :value="2">
                <v-row class="fill-height">
                  <v-col cols="12" md="4" class="deep-purple accent-4">
                    <v-card-text class="white--text mt-12">
                      <h1 class="text-center display-1">Welcome Back!</h1>
                      <h5 class="text-center">
                        To keep connection with us, please, login with your
                        personal data.
                      </h5>
                    </v-card-text>
                    <div class="text-center">
                      <v-btn rounded outlined dark @click="step--">
                        SIGN IN
                      </v-btn>
                    </div>
                  </v-col>
                  <v-col cols="12" md="8">
                    <v-card-text class="mt-12">
                      <h1 class="text-center display-2">Create Account!</h1>
                      <h4 class="text-center mt-4">
                        Ensure your email for registration
                      </h4>
                      <v-form>
                        <v-text-field
                          v-model="username"
                          v-on:keyup.enter="signUp"
                          label="Name"
                          name="name"
                          prepend-icon="person"
                          type="text"
                          color="deep-purple accent-4"
                          required
                        />
                        <v-text-field
                          v-model="email"
                          v-on:keyup.enter="signUp"
                          label="Email"
                          name="email"
                          prepend-icon="email"
                          type="text"
                          color="deep-purple accent-4"
                          required
                        />
                        <v-text-field
                          v-model="password"
                          v-on:keyup.enter="signUp"
                          label="Password"
                          name="password"
                          prepend-icon="lock"
                          type="password"
                          color="deep-purple accent-4"
                          required
                        />
                      </v-form>
                    </v-card-text>
                    <div class="text-center mt-n5">
                      <v-btn
                        rounded
                        color="deep-purple accent-4"
                        dark
                        @click="signUp"
                      >
                        SIGN UP
                      </v-btn>
                    </div>
                  </v-col>
                </v-row>
              </v-window-item>
            </v-window>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </v-main>
</template>

<script>
/* eslint-disable */
export default {
  // middleware: 'toMain', // check is user auth
  props: {
    source: String,
  },

  data: () => ({
    step: 1,

    email: '',
    username: '',
    password: '',
  }),
  mounted() {
    console.log(this.$store.getters.getToken)
  },
  methods: {
    signUp() {
      this.$store.dispatch('signUp', {
        email: this.email,
        username: this.username,
        password: this.password,
      })
    },
    signIn() {
      this.$store.dispatch('signIn', {
        username: this.username,
        password: this.password,
      }).then(() => {
        console.log('kek')
        this.$router.push('/main')
      })
    },
  },
}
</script>
