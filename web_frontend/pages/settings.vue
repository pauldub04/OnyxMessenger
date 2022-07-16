<template>
  <!-- <v-list-item>
    <v-list-item-content>
      <v-list-item-title class="font-weight bold">Dark Mode</v-list-item-title>
    </v-list-item-content>
    <v-list-item-action>
      <v-switch v-model="$vuetify.theme.dark"></v-switch>
    </v-list-item-action>
  </v-list-item> -->

  <v-row no-gutters>
    <NavigationDrawer
      :username="$store.state.user.username"
      :email="$store.state.user.email"
    ></NavigationDrawer>
    <v-col>
      <v-container fill-height>
        <v-card class="mx-auto" max-width="606">
          <v-card-title
            ><h2>{{ $t('pages.settings.label') }}</h2></v-card-title
          >

          <v-list subheader three-line>
            <v-subheader>{{ $t('pages.settings.apperance') }}</v-subheader>

            <v-list-item>
              <v-list-item-content>
                <v-list-item-title
                  ><h3>
                    {{ $t('pages.settings.colorDarkMode') }}
                  </h3></v-list-item-title
                >
                <v-col>
                  <v-row justify="start">
                    <v-switch v-model="isDark" class="mt-2 ml-4"></v-switch>
                  </v-row>
                  <v-row justify="start"
                    ><v-menu
                      v-model="menu"
                      :close-on-content-click="false"
                      :nudge-width="200"
                      offset-y
                    >
                      <template v-slot:activator="{ on }">
                        <v-btn text v-on="on">
                          {{ $t('pages.settings.changeColorButton') }}
                        </v-btn>
                      </template>
                      <v-card
                        v-for="(theme, index) in themes"
                        :key="index"
                        class="my-2"
                        :disabled="$vuetify.theme.themes.name === theme.name"
                        hover
                        outlined
                        @click="setTheme(theme)"
                      >
                        <v-list-item>
                          <v-list-item-content>
                            <v-list-item-title class="font-weight-bold">
                              {{ theme.name }}</v-list-item-title
                            >
                          </v-list-item-content>
                          <v-list-item-action>
                            <v-avatar
                              v-if="$vuetify.theme.themes.name === theme.name"
                              color="success"
                              size="30"
                            >
                              <v-icon>mdi-check</v-icon>
                            </v-avatar>
                          </v-list-item-action>
                        </v-list-item>
                        <div class="my-2">
                          <v-chip
                            v-for="(key, index2) in Object.keys(theme.dark)"
                            :key="index2"
                            class="mx-1"
                            label
                            :color="theme.dark[key]"
                          >
                            {{ key }}</v-chip
                          >
                        </div>
                        <div class="my-2">
                          <v-chip
                            v-for="(key, index2) in Object.keys(theme.light)"
                            :key="index2"
                            class="mx-1"
                            label
                            :color="theme.light[key]"
                          >
                            {{ key }}</v-chip
                          >
                        </div>
                      </v-card>
                    </v-menu>
                  </v-row>
                </v-col>
                <v-list-item-title
                  ><h3>
                    {{ $t('pages.settings.changeLanguage') }}
                  </h3></v-list-item-title
                >
                <v-menu
                  v-model="menuLang"
                  :close-on-content-click="false"
                  :nudge-width="50"
                  offset-y
                >
                  <template v-slot:activator="{ on }">
                    <v-btn text v-on="on">
                      <v-list-item>
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
                      @click="setLocale(locale.code)"
                    >
                      <v-list-item-avatar
                        ><v-img :src="locale.flagSrc"></v-img
                      ></v-list-item-avatar>
                      <v-list-item-content>{{
                        locale.name
                      }}</v-list-item-content>
                    </v-list-item>
                  </v-list>
                </v-menu>
              </v-list-item-content>
            </v-list-item>
          </v-list>
        </v-card>
      </v-container>
    </v-col>
  </v-row>
</template>

<script>
import { mdiCheck } from '@mdi/js'
import colors from 'vuetify/es5/util/colors'
import NavigationDrawer from '~/components/NavigationDrawer'
export default {
  name: 'Settings',
  components: { NavigationDrawer },
  data: () => ({
    menu: false,
    menuLang: false,
    icons: { check: mdiCheck },
    themes: [
      {
        name: 'Base Theme',
        dark: {
          primary: colors.blue.darken2,
          accent: colors.grey.darken3,
          secondary: colors.amber.darken3,
          info: colors.teal.lighten1,
          warning: colors.amber.base,
          error: colors.deepOrange.accent4,
          success: colors.green.accent3,
        },
        light: {
          primary: colors.blue.darken2,
          accent: colors.grey.darken3,
          secondary: colors.amber.darken3,
          info: colors.teal.lighten1,
          warning: colors.amber.base,
          error: colors.deepOrange.accent4,
          success: colors.green.accent3,
        },
      },
      {
        name: 'Theme 1',
        dark: {
          primary: '#21CFF3',
          accent: '#FF4081',
          secondary: '#21dc79',
          success: '#86af3f',
          info: '#f34fc6',
          warning: '#FB8C00',
          error: '#FF5252',
        },
        light: {
          primary: '#22daff',
          accent: '#ff6b99',
          secondary: '#26ff8c',
          success: '#a5d64c',
          info: '#ff53d0',
          warning: '#ff8e00',
          error: '#ff5252',
        },
      },
      {
        name: 'Theme 2',
        dark: {
          primary: '#E65100',
          accent: '#7CB342',
          secondary: '#689F38',
          success: '#4CAF50',
          info: '#6156d8',
          warning: '#1565C0',
          error: '#FF7043',
        },
        light: {
          primary: '#ffa450',
          accent: '#a1e754',
          secondary: '#92de4e',
          success: '#6dff74',
          info: '#7365ff',
          warning: '#2e8ac0',
          error: '#ff5e3c',
        },
      },
    ],
    isDark: false,
  }),
  computed: {
    availableLocales() {
      return this.$i18n.locales.filter((i) => i.code !== this.$i18n.locale)
    },
  },
  watch: {
    isDark() {
      this.$vuetify.theme.dark = this.isDark
      localStorage.setItem('dark_theme', this.isDark)
    },
  },
  updated() {
    console.log('set theme')
    this.$store.dispatch('setTheme', this.$i18n)
  },
  mounted() {
    this.isDark = JSON.parse(localStorage.getItem('dark_theme')) || 0
  },
  methods: {
    setTheme(theme) {
      localStorage.setItem('theme', JSON.stringify(theme))
      this.$store.dispatch('setTheme', this.$i18n)
      this.menu = false
    },
    setLocale(code) {
      localStorage.setItem('locale', JSON.stringify(code))
      this.$store.dispatch('setTheme', this.$i18n)
    },
  },
}
</script>
