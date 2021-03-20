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
            <v-row justify="center" class="mt-6">
              <v-form @submit="signIn">
                <v-row justify="center">
                  <v-text-field
                    v-model="username"
                    label="Username"
                    rounded
                    dense
                    outlined
                  >
                  </v-text-field>
                </v-row>
                <v-row justify="center">
                  <v-text-field
                    v-model="password"
                    label="Password"
                    rounded
                    dense
                    outlined
                  >
                  </v-text-field>
                </v-row>
                <v-row justify="center">
                  <v-btn type="submit"> Submit </v-btn>
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
  </v-app>
</template>

<script>
export default {
  data: () => ({
    username: '',
    password: '',
  }),
  methods: {
    setHeight() {
      const height = window.innerHeight
      return 'height: ' + height
    },
    signIn() {
      // eslint-disable-next-line no-console
      console.log('Shit')
    },
  },
}
</script>

<style></style>
