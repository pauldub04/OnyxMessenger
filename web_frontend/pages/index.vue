<template>
  <v-app>
    <v-container>
      <v-toolbar>
        <v-toolbar-title>Messenger</v-toolbar-title>
        <v-spacer></v-spacer>
        About Us
      </v-toolbar>
    </v-container>

    <v-row align="center">
      <v-col>
        <v-row>
          <v-col cols="5">
            <v-row justify="center" align="start">
              <h1>LOG IN</h1>
            </v-row>
            <v-row justify="center" class="mt-10">
              <!-- <v-form @submit="signIn"> -->
              <v-form @submit.prevent="signIn" v-model="valid">
                <v-row justify="center">
                  <v-text-field
                    v-model="username"
                    label="Username"
                    rounded
                    dense
                    outlined
                    required
                    :rules="rules.required"
                  >
                  </v-text-field>
                </v-row>
                <v-row justify="center">
                  <v-text-field
                    v-model="password"
                    label="Password"
                    :type="showPassword ? 'text' : 'password'"
                    :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
                    rounded
                    dense
                    outlined
                    required
                    :rules="rules.required"
                    @click:append="showPassword = !showPassword"
                  >
                  </v-text-field>
                </v-row>
                <v-row justify="center">
                  <v-btn type="submit" :disabled="!valid"> Submit </v-btn>
                </v-row>
              </v-form>
            </v-row>
          </v-col>
          <v-col align-self="center">
            <v-row justify="center"><h2>or</h2></v-row>
          </v-col>
          <v-col cols="5">
            <v-row justify="center" align="center"><h1>SIGN UP</h1></v-row>
            <v-container fill-height>
              <v-row align="center" justify="center">
                <v-btn to="/registration">GO TO FORM</v-btn>
              </v-row>
            </v-container>
          </v-col>
        </v-row>
      </v-col>
    </v-row>

    <!-- <v-row class="mr-0">
      <v-col cols="3" align-self="end" offset-md="9">
        <v-alert dismissible type="error" elevation="6" text disable>
          kek
        </v-alert>
      </v-col>
    </v-row> -->
    <!-- <v-snackbar v-model="snackbar">
      {{ error }}

      <template v-slot:action="{ attrs }">
        <v-btn color="red" text v-bind="attrs" @click="snackbar = false">
          Close
        </v-btn>
      </template>
    </v-snackbar> -->
  </v-app>
</template>

<script>
export default {
  data: () => ({
    username: '',
    password: '',

    valid: true,
    showPassword: false,
    rules: {
      required: [(value) => !!value || 'This field is required'],
    },

    // snackbar: false,
    // text: `I'm a multi-line snackbar.`,
  }),
  methods: {
    setHeight() {
      const height = window.innerHeight
      return 'height: ' + height
    },
    signIn() {
      this.$store.dispatch('signIn', {
        username: this.username,
        password: this.password,
      })
    },
  },
}
</script>

<style></style>
