export default {
  username: 'Никнейм',
  password: 'Пароль',
  fieldRequired: 'Это поле должно быть заполнено',
  submit: 'Отправить',
  emailRequired: 'E-mail должен быть заполнен',
  emailNotValid: 'E-mail доолжен быть валидным',
  passwordMin: 'Минимум 8 символов',
  pages: {
    landPage: {
      logIn: 'ВОЙТИ',
      or: 'или',
      signUp: 'ЗАРЕГИСТРИРОВАТЬСЯ',
      goToForm: 'Перейти к форме',
    },
    registrationPage: {
      back: 'Назад',
      next: 'Вперед',
      signUp: 'Зарегистрироваться',
      setUsername: {
        title: 'Введите ваш никнейм',
        placeholder: 'Никнейм',
        explanation:
          'Этот ник будет отображаться в вашем главном меню и у пользователей, с которыми вы будете общаться.',
      },
      setEmail: {
        title: 'Введите ваш E-mail',
        placeholder: 'E-mail',
        explanation:
          'Если вы потеряете свой пароль, вы можете восстановить его по электронной почте.',
      },
      setPassword: {
        title: 'Введите ваш пароль',
        placeholder: 'Пароль',
        confirmPlaceholder: 'Подтвердите пароль',
        explanation: 'Используйте пароль для подтверждения своей личности',
        hint: 'Как минимум 8 символов',
      },
      checkData: {
        title: 'Почти готово',
        subTitle: 'Вы так близки!',
        explanation: 'Проверьте свои данные перед регистрацией!',
      },
    },
    NavigationDrawer: {
      chats: 'Чаты',
      settings: 'Настройки',
      createChat: 'Создайте чат',
      logOut: 'Выйти из аккаунта',
    },
    settings: {
      label: 'Настройки',
      apperance: 'Визуальное оформление',
      colorDarkMode: 'Темная тема и цветовое оформление',
      changeColorButton: 'Изменить цветовое оформление',
      changeLanguage: 'Изменить язык',
    },
    createChat: {
      label: 'Создать чат',
      stepOne: {
        stepLabel: 'Выберите тип чата:',
        privateMessages: 'Личные сообщение',
        groupChat: 'Групповой чат',
      },
      stepTwo: {
        stepLabel: 'Добавьте друзей:',
        placeholderOne: 'Введите никнейм',
        placeholderTwo: 'Введите никнеймы',
      },
      continue: 'Продолжить',
      createChat: 'Создать чат',
      cancel: 'Назад',
    },
  },
}
