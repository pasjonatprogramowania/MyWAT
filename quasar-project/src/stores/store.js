import { defineStore } from 'pinia'
import axios from 'axios'

export const usePointsStore = defineStore('points', {
  state: () => ({
    points: [],
  }),

  actions: {
    // async fetchPoints() {
    //   try {
    //     const response = await axios.get('/api/points')
    //     this.points = response.data
    //   } catch (error) {
    //     console.error('Błąd podczas pobierania punktów:', error)
    //   }
    // },
  },
})
