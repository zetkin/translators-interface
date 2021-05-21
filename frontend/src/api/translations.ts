import { Translation, TranslationPostBody } from '../global.types'
import fetchWrapper from './fetchWrapper'

export const getTranslations = async (
  project_id: number | string,
  language_id: number | string
): Promise<Translation[]> => {
  return fetchWrapper({
    url: `${process.env.NEXT_PUBLIC_API_HOST}/translations/?project=${project_id}&language=${language_id}`,
  })
}

export const postTranslation = async (
  translation: TranslationPostBody
): Promise<Translation> => {
  const body = JSON.stringify(translation)
  return fetchWrapper({
    method: 'POST',
    url: `${process.env.NEXT_PUBLIC_API_HOST}/translations/`,
    body,
  })
}
