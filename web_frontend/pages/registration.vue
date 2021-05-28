<template>
  <v-main>
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
              v-for="locale in availableLocales"
              :key="locale.code"
              link
              hover
              @click="$i18n.setLocale(locale.code)"
            >
              <v-list-item-avatar
                ><v-img :src="locale.flagSrc"></v-img
              ></v-list-item-avatar>
              <v-list-item-content>{{ locale.name }}</v-list-item-content>
            </v-list-item>
          </v-list>
        </v-menu>
      </v-toolbar>
    </v-container>

    <v-container fill-height>
      <v-card class="mx-auto" max-width="500">
        <v-card-title class="title font-weight-regular justify-space-between">
          <span v-if="this.step === 1">{{
            $t('pages.registrationPage.setUsername.title')
          }}</span>
          <span v-else-if="this.step === 2">{{
            $t('pages.registrationPage.setEmail.title')
          }}</span>
          <span v-else-if="this.step === 3">{{
            $t('pages.registrationPage.setPassword.title')
          }}</span>
          <span v-else>{{ $t('pages.registrationPage.checkData.title') }}</span>
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
                :label="$t('pages.registrationPage.setUsername.placeholder')"
                :rules="[(value) => !!value || $t('fieldRequired')]"
                required
              ></v-text-field>
              <span class="caption grey--text text--darken-1">
                {{ $t('pages.registrationPage.setUsername.explanation') }}
              </span>
            </v-card-text>
          </v-window-item>

          <v-window-item :value="2">
            <v-card-text>
              <v-text-field
                v-model="email"
                :label="$t('pages.registrationPage.setEmail.placeholder')"
                :rules="[
                  (v) => !!v || $t('emailRequired'),
                  (v) => /.+@.+\..+/.test(v) || $t('emailNotValid'),
                ]"
              ></v-text-field>
              <span class="caption grey--text text--darken-1">
                {{ $t('pages.registrationPage.setEmail.explanation') }}
              </span>
            </v-card-text>
          </v-window-item>

          <v-window-item :value="3">
            <v-card-text>
              <v-text-field
                v-model="password"
                :label="$t('pages.registrationPage.setPassword.placeholder')"
                :append-icon="show ? 'mdi-eye' : 'mdi-eye-off'"
                :rules="[
                  (value) => !!value || $t('fieldRequired'),
                  (value) => value.length >= 8 || $t('passwordMin'),
                ]"
                :type="show ? 'text' : 'password'"
                name="input-10-1"
                :hint="$t('pages.registrationPage.setPassword.hint')"
                counter
                @click:append="show = !show"
              ></v-text-field>
              <v-text-field
                v-model="confirm_password"
                :label="
                  $t('pages.registrationPage.setPassword.confirmPlaceholder')
                "
                :type="show ? 'text' : 'password'"
                name="input-10-1"
                counter
              ></v-text-field>
              <span class="caption grey--text text--darken-1">
                {{ $t('pages.registrationPage.setPassword.explanation') }}
              </span>
            </v-card-text>
          </v-window-item>

          <v-window-item :value="4">
            <div class="pa-4 text-center">
              <h3 class="title font-weight-light mb-2">
                {{ $t('pages.registrationPage.checkData.subTitle') }}
              </h3>
              <span class="caption grey--text">
                {{ $t('pages.registrationPage.checkData.explanation') }}
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
          <v-btn text @click="back">
            {{ $t('pages.registrationPage.back') }}
          </v-btn>
          <v-spacer></v-spacer>
          <v-btn
            v-if="step === 1"
            :disabled="username === ''"
            color="primary"
            depressed
            @click="step++"
            >{{ $t('pages.registrationPage.next') }}</v-btn
          >
          <v-btn
            v-else-if="step === 2"
            :disabled="!checkEmail"
            color="primary"
            depressed
            @click="step++"
            >{{ $t('pages.registrationPage.next') }}</v-btn
          >
          <v-btn
            v-else-if="step === 3"
            :disabled="
              confirm_password === '' ||
              password === '' ||
              password !== confirm_password
            "
            color="primary"
            depressed
            @click="step++"
          >
            {{ $t('pages.registrationPage.next') }}
          </v-btn>
          <v-btn v-else color="primary" depressed @click="signUp">
            {{ $t('pages.registrationPage.signUp') }}
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-container>
  </v-main>
</template>

<script>
export default {
  name: 'Registration',
  data: () => ({
    menu: false,
    step: 1,
    show: false,
    showAgreement: false,
    username: '',
    password: '',
    email: '',
    confirm_password: '',
    rules: {
      required: (value) => !!value || 'This field is required',
      min: (value) => value.length >= 8 || 'Min 8 characters',
      email: [
        (v) => !!v || 'E-mail is required',
        (v) => /.+@.+\..+/.test(v) || 'E-mail must be valid',
      ],
    },
  }),
  computed: {
    checkEmail() {
      return /.+@.+\..+/.test(this.email) && !!this.email
    },
    availableLocales() {
      return this.$i18n.locales.filter((i) => i.code !== this.$i18n.locale)
    },
  },
  beforeCreate() {
    this.$store.dispatch('middlewareAuthSign')
  },
  methods: {
    signUp() {
      this.$store.dispatch('signUp', {
        email: this.email,
        username: this.username,
        password: this.password,
      })
    },
    back() {
      if (this.step === 1) this.$router.push(this.localePath('/'))
      else this.step--
    },
  },
}
</script>

<style scoped></style>
