<template>
  <v-app>
    <v-container>
      <v-toolbar>
        <v-toolbar-title>ONYX - the Messenger</v-toolbar-title>
        <v-spacer></v-spacer>
        <v-menu
          v-model="menu"
          :close-on-content-click="false"
          :nudge-width="50"
          offset-y
        >
          <template v-slot:activator="{ on }">
            <v-btn text v-on="on">
              <v-list-item>
                <v-list-item-avatar
                  ><v-img
                    :src="
                      $i18n.locale === 'en'
                        ? 'https://cdn.vuetifyjs.com/images/flags/us.png'
                        : 'https://cdn.vuetifyjs.com/images/flags/ru.png'
                    "
                  ></v-img
                ></v-list-item-avatar>
                <v-list-item-content>{{
                  $i18n.locale === 'en' ? 'English' : 'Русский'
                }}</v-list-item-content>
              </v-list-item>
            </v-btn>
          </template>

          <v-list>
            <v-list-item
              v-for="(language, index) in languages"
              :key="index"
              link
              hover
              @click="changeLanguage(language)"
            >
              <v-list-item-avatar
                ><v-img :src="language.flagSrc"></v-img
              ></v-list-item-avatar>
              <v-list-item-content>{{ language.title }}</v-list-item-content>
            </v-list-item>
          </v-list>
        </v-menu>
      </v-toolbar>
    </v-container>

    <v-row align="center">
      <v-col>
        <v-row>
          <v-col cols="5">
            <v-row justify="center" align="start">
              <h1>{{ $t('pages.landPage.logIn') }}</h1>
            </v-row>
            <v-row justify="center" class="mt-10">
              <!-- <v-form @submit="signIn"> -->
              <v-form v-model="valid" @submit.prevent="signIn">
                <v-row justify="center">
                  <v-text-field
                    v-model="username"
                    :label="$t('username')"
                    rounded
                    dense
                    outlined
                    required
                    :rules="[(value) => !!value || $t('fieldRequired')]"
                  >
                  </v-text-field>
                </v-row>
                <v-row justify="center">
                  <v-text-field
                    v-model="password"
                    :label="$t('password')"
                    :type="showPassword ? 'text' : 'password'"
                    :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
                    rounded
                    dense
                    outlined
                    required
                    :rules="[(value) => !!value || $t('fieldRequired')]"
                    @click:append="showPassword = !showPassword"
                  >
                  </v-text-field>
                </v-row>
                <v-row justify="center">
                  <v-btn type="submit" :disabled="!valid">
                    {{ $t('submit') }}
                  </v-btn>
                </v-row>
              </v-form>
            </v-row>
          </v-col>
          <v-col align-self="center">
            <v-row justify="center"
              ><h2>{{ $t('pages.landPage.or') }}</h2></v-row
            >
          </v-col>
          <v-col cols="5">
            <v-row justify="center" align="center"
              ><h1>{{ $t('pages.landPage.signUp') }}</h1></v-row
            >
            <v-container fill-height>
              <v-row align="center" justify="center">
                <v-btn :to="localePath('/registration')">{{
                  $t('pages.landPage.goToForm')
                }}</v-btn>
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
    languages: [
      {
        iso: 'en',
        title: 'English',
        flagSrc: 'https://cdn.vuetifyjs.com/images/flags/us.png',
      },
      {
        iso: 'ru',
        title: 'Русский',
        flagSrc: 'https://cdn.vuetifyjs.com/images/flags/ru.png',
      },
    ],

    username: '',
    password: '',

    menu: false,

    valid: true,
    showPassword: false,

    // snackbar: false,
    // text: `I'm a multi-line snackbar.`,
  }),
  beforeCreate() {
    this.$store.dispatch('middlewareAuthSign')
  },
  mounted() {
    this.$store.dispatch('setTheme', this.$i18n)
  },
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
    changeLanguage(language) {
      this.menu = false
      this.$i18n.locale = language.iso
    },
  },
}
</script>

<style></style>
