import { GetStaticProps, GetStaticPaths, NextPage } from 'next'
import Head from 'next/head'

import { Container, TableRow, TableCell } from '@material-ui/core'

import { Translation, Project, Language } from '../../../src/global.types'
import { getProject, getProjects } from '../../../src/api/projects'
import TranslationField from '../../../src/components/TranslationField'
import { getTranslations } from '../../../src/api/translations'
import joinTranslations, {
  JoinedTranslation,
} from '../../../src/utils/joinTranslations'

import style from './[language_code].module.css'

/**
 * Translations Page - Page for viewing and editing translations
 */

interface StaticProps {
  project: Project
  translations: Translation[]
  englishTranslations: Translation[]
  joinedTranslations: JoinedTranslation[]
  selectedLanguage: Language
}

export const getStaticPaths: GetStaticPaths = async () => {
  const projects = await getProjects()

  const paths = projects.reduce((acc, project) => {
    return [
      ...acc,
      ...project.languages.map(
        (language) => `/projects/${project.id}/${language.language_code}`
      ),
    ]
  }, [])

  return {
    paths,
    fallback: true,
  }
}

export const getStaticProps: GetStaticProps<
  StaticProps,
  { id: string; language_code: string }
> = async ({ params }) => {
  const project = await getProject(params.id)

  const selectedLanguage = project.languages.find(
    (language) => language.language_code === params.language_code
  )
  const english = project.languages.find(
    (language) => language.language_code === 'en'
  )

  const translations = await getTranslations(
    parseInt(params.id),
    selectedLanguage.id
  )
  const englishTranslations = await getTranslations(
    parseInt(params.id),
    english.id
  )

  const joinedTranslations = joinTranslations(englishTranslations, translations)

  return {
    props: {
      project,
      translations,
      englishTranslations,
      joinedTranslations,
      selectedLanguage,
    },
  }
}

const ProjectPage: NextPage<StaticProps> = ({
  project,
  selectedLanguage,
  joinedTranslations,
}) => {
  return (
    <div>
      <Head>
        <title>Zetkin Translators Interface</title>
        <meta name="description" content="Editing translations" />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main>
        <Container style={{ marginTop: 20, marginBottom: 20 }} maxWidth="xl">
          <div
            style={{
              display: 'grid',
              gridTemplateColumns: 'auto 1fr 1fr',
              gridTemplateRows: 'auto',
              alignItems: 'center',
            }}
          >
            <div className={style.gridCell}>
              <b>
                <code>Dotpath</code>
              </b>
            </div>
            <div className={style.gridCell}>
              <b>English</b>
            </div>
            <div className={style.gridCell}>
              <b>Swedish</b>
            </div>

            {joinedTranslations.map((joinedTranslation) => {
              return (
                <>
                  <div className={style.gridCell}>
                    <code>{joinedTranslation.english.dotpath}</code>
                  </div>
                  <div className={style.gridCell}>
                    {joinedTranslation.english.text}
                  </div>
                  <div className={style.gridCell}>
                    <TranslationField
                      base={joinedTranslation.english}
                      selected={joinedTranslation.selected}
                    />
                  </div>
                </>
              )
            })}
          </div>
        </Container>
      </main>
    </div>
  )
}

export default ProjectPage
