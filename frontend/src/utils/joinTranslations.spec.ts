import { Translation } from '../global.types'
import joinTranslations from './joinTranslations'

// English translations
const englishTranslations = [
  {
    dotpath: 'h1',
  },
  {
    dotpath: 'h2',
  },
  {
    dotpath: 'h3',
  },
]

const swedishTranslations = [
  {
    dotpath: 'h1',
  },
  {
    dotpath: 'h2',
  },
  {
    dotpath: 'h3',
  },
]

// Swedish translations match

describe('joinTranslations()', () => {
  it('Joins matching lists of translations', () => {
    const joinedTranslations = joinTranslations(
      // @ts-ignore
      englishTranslations,
      // @ts-ignore
      swedishTranslations
    )

    console.log(joinedTranslations)

    expect(joinedTranslations.length).toEqual(3)

    joinedTranslations.forEach((joinedTranslation) => {
      expect(joinedTranslation.english.dotpath).toEqual(
        joinedTranslation.selected.dotpath
      )
    })
  })
})
