<template>
  <v-row no-gutters>
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
      <v-col>
        <h1 v-if="error.statusCode === 404">{{ $t('error404') }}</h1>
        <h1 v-else>{{ $t('errorOccured') }}</h1>
        <NuxtLink class="text-decoration-none" :to="localePath('/main')">{{
          $t('toHome')
        }}</NuxtLink>
      </v-col>
    </v-container>
  </v-row>
</template>

<script>
export default {
  props: ['error'],
  data: () => ({
    menu: false,
  }),
  computed: {
    availableLocales() {
      return this.$i18n.locales.filter((i) => i.code !== this.$i18n.locale)
    },
  },
}
</script>

<style></style>
