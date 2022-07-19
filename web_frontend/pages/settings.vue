<!-- eslint-disable -->
<template>

  <v-row no-gutters>
    <NavigationDrawer
      :username="$store.state.user.username"
      :email="$store.state.user.email"
    ></NavigationDrawer>

    <v-container fill-height>
      <v-row>
        <v-col cols="7" class="mx-auto">
          <v-card>
            <v-card-title>{{ $t('pages.settings.label') }}</v-card-title>
            <v-card-subtitle>{{ $t('pages.settings.apperance') }}</v-card-subtitle>

            <v-list>
              <v-list-item @click="isDark = !isDark">
                <v-row class="py-2">
                  <v-col class="mt-2">
                    {{ $t('pages.settings.colorDarkMode') }}
                  </v-col>
                  <v-spacer></v-spacer>
                  <v-switch readonly class="mr-2" v-model="isDark"></v-switch>
                </v-row>
              </v-list-item>

              <v-divider light class="mx-4 mt-2"></v-divider>

              <v-list>
                <v-list-group>
                  <template v-slot:activator>
                    <v-list-item-content>
                      <v-list-item-title class="py-2">{{ $t('pages.settings.changeColorButton') }}</v-list-item-title>
                    </v-list-item-content>
                  </template>

                  <v-list-item
                    v-for="(theme, index) in themes"
                    :key="index"
                    @click="setTheme(theme)"
                    :disabled="selectedThemeName === theme.name"
                  >
                    <v-list-item-content>
                      <v-row>
                        <v-col cols="3" class="mt-4">
                          <v-list-item-title>{{ $t('pages.settings.themeName') }} {{ index+1 }}</v-list-item-title>
                        </v-col>
                        <v-col class="mx-0 px-0">
                          <v-sheet
                            :color="theme.dark.primary"
                            height="50"
                          ></v-sheet>
                        </v-col>
                        <v-col class="mx-0 px-0">
                          <v-sheet
                            :color="theme.dark.accent"
                            height="50"
                          ></v-sheet>
                        </v-col>
                      </v-row>
                    </v-list-item-content>
                  </v-list-item>

                </v-list-group>
              </v-list>

              <v-divider light class="mx-4"></v-divider>

              <v-list-item class="my-2">
                <v-list-item-title>
                  {{ $t('pages.settings.changeLanguage') }}
                </v-list-item-title>
                <v-menu
                  v-model="menuLang"
                  offset-y
                >
                  <template v-slot:activator="{ on }">
                    <v-btn plain tile v-on="on">{{ $i18n.locale === 'en' ? 'English' : 'Русский' }}</v-btn>
                  </template>

                  <v-list>
                    <v-list-item
                      v-for="locale in availableLocales"
                      :key="locale.code"
                      link
                      hover
                      @click="setLocale(locale.code)"
                    >
                      <v-img :src="locale.flagSrc" contain max-width="15" class="mr-3"></v-img>
                      <v-list-item-content>{{ locale.name }}</v-list-item-content>
                    </v-list-item>
                  </v-list>
                </v-menu>
              </v-list-item>

            </v-list>
          </v-card>
        </v-col>
      </v-row>
    </v-container>

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
    selectedThemeName: 'Base Theme',
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
    this.selectedThemeName = this.$vuetify.theme.themes.name
  },
  mounted() {
    this.isDark = JSON.parse(localStorage.getItem('dark_theme')) || 0
    this.selectedThemeName = this.$vuetify.theme.themes.name

    console.log(this.$i18n.locales)
  },
  methods: {
    setTheme(theme) {
      localStorage.setItem('theme', JSON.stringify(theme))
      this.$store.dispatch('setTheme', this.$i18n)
      this.menu = false
      setTimeout(() => {
        this.selectedThemeName = theme.name
      }, 300)
    },
    setLocale(code) {
      localStorage.setItem('locale', JSON.stringify(code))
      this.$store.dispatch('setTheme', this.$i18n)
    },
  },
}
</script>
