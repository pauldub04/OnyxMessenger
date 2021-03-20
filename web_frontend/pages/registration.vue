<template>
  <v-container fill-height>
    <v-container>
      <v-card class="mx-auto" max-width="500">
        <v-card-title class="title font-weight-regular justify-space-between">
          <span>{{ currentTitle }}</span>
          <v-avatar
            color="primary lighten-2"
            class="subheading white--text"
            size="24"
            v-text="step"
          ></v-avatar>
        </v-card-title>

        <v-window v-model="step">
          <v-window-item :value="1">
            <v-card-text>
              <v-text-field
                v-model="username"
                label="Username"
                :rules="rules[rules.required]"
              ></v-text-field>
              <span class="caption grey--text text--darken-1">
                This is the username you will use to login to your account
              </span>
            </v-card-text>
          </v-window-item>

          <v-window-item :value="2">
            <v-card-text>
              <v-text-field
                v-model="password"
                label="Password"
                :append-icon="show ? 'mdi-eye' : 'mdi-eye-off'"
                :rules="[rules.required, rules.min]"
                :type="show ? 'text' : 'password'"
                name="input-10-1"
                hint="At least 8 characters"
                counter
                @click:append="show = !show"
              ></v-text-field>
              <v-text-field
                v-model="confirm_password"
                label="Confirm Password"
                type="text"
                name="input-10-1"
                counter
              ></v-text-field>
              <span class="caption grey--text text--darken-1">
                Please enter a password for your account
              </span>
            </v-card-text>
          </v-window-item>

          <v-window-item :value="3">
            <div class="pa-4 text-center">
              <h3 class="title font-weight-light mb-2">You are so close!</h3>
              <span class="caption grey--text">
                Check your data before you sign up!
              </span>
              <v-text-field v-model="username" readonly></v-text-field>
              <v-text-field
                v-model="password"
                readonly
                :append-icon="showAgreement ? 'mdi-eye' : 'mdi-eye-off'"
                :type="showAgreement ? 'text' : 'password'"
                @click:append="showAgreement = !showAgreement"
              ></v-text-field>
            </div>
          </v-window-item>
        </v-window>

        <v-divider></v-divider>

        <v-card-actions>
          <v-btn :disabled="step === 1" text @click="step--"> Back </v-btn>
          <v-spacer></v-spacer>
          <v-btn
            v-if="step === 1"
            :disabled="username === ''"
            color="primary"
            depressed
            @click="step++"
            >NEXT</v-btn
          >
          <v-btn
            v-else-if="step === 2"
            :disabled="
              confirm_password === '' ||
              password === '' ||
              password !== confirm_password
            "
            color="primary"
            depressed
            @click="step++"
          >
            Next
          </v-btn>
          <v-btn v-else color="primary" depressed @click="registerAccount">
            SIGN UP
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-container>
  </v-container>
</template>

<script>
export default {
  name: 'Registration',
  data: () => ({
    step: 1,
    show: false,
    showAgreement: false,
    username: '',
    password: '',
    confirm_password: '',
    rules: {
      required: (value) => !!value || 'Required.',
      min: (value) => value.length >= 8 || 'Min 8 characters',
    },
  }),

  computed: {
    currentTitle() {
      switch (this.step) {
        case 1:
          return 'Set your username'
        case 2:
          return 'Set your password'
        default:
          return 'Almost done'
      }
    },
  },
  methods: {
    registerAccount() {
      // eslint-disable-next-line no-console
      console.log('SHit')
    },
  },
}
</script>

<style scoped></style>
