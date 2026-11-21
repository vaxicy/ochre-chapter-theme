// Ochre & Chapter Theme — four autumn chapters
import { readFile } from 'node:fs/promises';

const CHAPTERS = {
  knit: '#337E63',
  christmas: '#B11111',
  cookie: '#B4754E',
  leaves: '#62561B',
  paper: '#F2F3D2',
  ink: '#2A1210',
};

export class Almanac {
  constructor(season = 'Autumn') {
    this.season = season;
    this.palette = CHAPTERS;
    this.chapters = Object.keys(CHAPTERS).filter((k) => k !== 'paper' && k !== 'ink');
  }

  blend(from, to, ratio = 0.5) {
    const parse = (hex) => [1, 3, 5].map((i) => parseInt(hex.slice(i, i + 2), 16));
    const [a, b] = [parse(from), parse(to)];
    return '#' + a.map((v, i) => Math.round(v * (1 - ratio) + b[i] * ratio)
      .toString(16).padStart(2, '0')).join('');
  }

  async readChapter(file) {
    const content = await readFile(file, 'utf8');
    return { season: this.season, chapters: this.chapters.length,
             lines: content.split('\n').filter(Boolean).length, content };
  }
}

const almanac = new Almanac();
console.log(`autumn shade: ${almanac.blend(CHAPTERS.knit, CHAPTERS.cookie)}`);
