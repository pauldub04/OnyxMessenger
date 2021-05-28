<template>
  <v-row no-gutters>
    <NavigationDrawer
      :username="$store.state.user.username"
      :email="$store.state.user.email"
    ></NavigationDrawer>
    <v-col justify="center">
      <v-container>
        <h1>{{ $t('pages.createChat.label') }}</h1>
        <v-stepper v-model="stepper" vertical>
          <v-stepper-step :complete="stepper > 1" step="1">
            {{ $t('pages.createChat.stepOne.stepLabel') }}
          </v-stepper-step>
          <v-stepper-content step="1">
            <v-radio-group v-model="newChatType" class="ml-2">
              <v-radio
                :label="$t('pages.createChat.stepOne.privateMessages')"
                :value="1"
              ></v-radio>
              <v-radio
                :label="$t('pages.createChat.stepOne.groupChat')"
                :value="2"
              ></v-radio>
            </v-radio-group>
            <v-btn
              class="mt-2"
              :disabled="newChatType === null"
              color="primary"
              @click="stepper = 2"
            >
              {{ $t('pages.createChat.continue') }}
            </v-btn>
          </v-stepper-content>
          <v-stepper-step :complete="stepper > 2" step="2">
            {{ $t('pages.createChat.stepTwo.stepLabel') }}
          </v-stepper-step>
          <v-stepper-content step="2">
            <v-container v-if="newChatType === 1">
              <v-autocomplete
                chips
                deletable-chips
                class="mt-4 mr-5"
                clearable
                :label="$t('pages.createChat.stepTwo.placeholderOne')"
              ></v-autocomplete>
            </v-container>
            <v-container v-else>
              <v-autocomplete
                chips
                deletable-chips
                multiple
                class="mt-4 mr-5"
                clearable
                :label="$t('pages.createChat.stepTwo.placeholderTwo')"
              ></v-autocomplete>
            </v-container>
            <v-btn color="primary">
              {{ $t('pages.createChat.createChat') }}
            </v-btn>
            <v-btn text @click="stepper = 1">
              {{ $t('pages.createChat.cancel') }}
            </v-btn>
          </v-stepper-content>
        </v-stepper>
      </v-container>
    </v-col>
  </v-row>
</template>

<script>
import NavigationDrawer from '~/components/NavigationDrawer'
export default {
  name: 'CreateChat',
  components: { NavigationDrawer },
  data: () => ({
    stepper: 1,
    newChatType: null,
    inviteUserName: null,
    users: [],
    chatType: [
      {
        name: 'Личные сообщения',
        val: 1,
      },
      {
        name: 'Групповой чат',
        val: 2,
      },
    ],
  }),
}
</script>
