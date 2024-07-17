-- phpMyAdmin SQL Dump
-- version 3.4.10.1
-- http://www.phpmyadmin.net
--
-- Host: localhost:3306
-- Erstellungszeit: 05. Apr 2012 um 11:25
-- Server Version: 5.1.56
-- PHP-Version: 5.3.8

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Datenbank: `ajax`
--

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `rjsautoren`
--

CREATE TABLE IF NOT EXISTS `rjsautoren` (
  `autor` varchar(50) NOT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=138 ;

--
-- Daten für Tabelle `rjsautoren`
--

INSERT INTO `rjsautoren` (`autor`, `id`) VALUES
('Abraham a Santa Clara', 1),
('Albert Camus', 2),
('		Alphonse Allais		', 3),
('		Antoine de Rivarol		', 4),
('		Archimedes		', 5),
('		Aristoteles		', 6),
('		Arthur Schnitzler		', 7),
('		Benjamin Franklin		', 8),
('		Blaise Pascal		', 9),
('		Clara Schumann		', 10),
('		Danny Kaye		', 11),
('		Eberhard von Kuenheim		', 12),
('		Eleonora Duse		', 13),
('		Elias Canetti		', 14),
('		Ella Wheeler Wilcox		', 15),
('		Florence Nightingale		', 16),
('		Franca Magnani		', 17),
('		François Mitterrand		', 18),
('		Franz Beckenbauer		', 19),
('		Franz von Assisi		', 20),
('		Friedrich Nietzsche		', 21),
('		Friedrich Schiller		', 22),
('		George Bernard Shaw		', 23),
('		George Gordon Noel Byron		', 24),
('		Gerhart Hauptmann		', 25),
('		Greta Garbo		', 26),
('		Gustav Knuth		', 27),
('		Harald Schmidt		', 28),
('		Heimito von Doderer		', 29),
('		Helmut Qualtinger		', 30),
('		Henry Brooks Adams		', 31),
('		Isaac Asimov		', 32),
('		Jacques Bénigne Bossuet		', 33),
('		Jakob Bosshart		', 34),
('		James Joyce		', 35),
('		Jawaharlal Nehru		', 36),
('		Jean Cocteau		', 37),
('		Jean-Jacques Rousseau		', 38),
('		Jeannette Rankin		', 39),
('		Johann Wolfgang von Goethe		', 40),
('		John B. Priestley		', 41),
('		John Brown		', 42),
('		John F. Kennedy		', 43),
('		John McEnroe		', 44),
('		John Osborne		', 45),
('		Jürgen Klinsmann		', 46),
('		Karl Ferdinand Gutzkow		', 47),
('		Karl Heinrich Waggerl		', 48),
('		Karl Marx		', 49),
('		Lucius Annaeus Seneca		', 50),
('		Ludwig Börne		', 51),
('		Mao Zedong		', 52),
('		Marcus Tullius Cicero		', 53),
('		Marie Curie		', 54),
('		Mark Twain		', 55),
('		Martin Kessel		', 56),
('		Niccolò Machiavelli		', 57),
('		Novalis		', 58),
('		Oswald Bumke		', 59),
('		Otto von Bismarck		', 60),
('		Platon		', 61),
('		Ralph Waldo Emerson		', 62),
('		Samuel Goldwyn		', 63),
('		Sokrates		', 64),
('		Sören Aabye Kierkegaard		', 65),
('		Stephen King		', 66),
('		Tennessee Williams		', 67),
('		Theodore Roosevelt		', 68),
('		Victor Hugo		', 69),
('		Voltaire		', 70),
('		Waldemar Bonsels		', 71),
('		Walther Rathenau		', 72),
('		Wilhelm Busch		', 73),
('		William Shakespeare		', 74),
('		Wladimir I. Lenin		', 75),
('		Wolfgang Amadeus Mozart		', 76),
('		Wolfram Weidner		', 77),
('		Woody Allen		', 78),
('	Christian Fürchtegott Gellert	', 79),
('	Guido Westerwellle 	', 80),
('	Konfuzius 	', 81),
('	Albert Schweitzer 	', 82),
('	Albert Einstein	', 83),
('Oscar Wilde', 84),
('Friedrich Josef Dürrenmatt ', 85),
('Sigmund Freud', 86),
('Heraklit', 87),
('Lothar Matthäus', 88),
('Edmund Stoiber', 89),
('Abraham Lincoln', 90),
('Aldous Huxley', 91),
('Anton Tschechow', 92),
('Arthur Schopenhauer', 93),
('Bertrand Russel', 94),
('Dieter Hildebrandt', 95),
('Erich Kästner', 96),
('Mahatma Gandhi', 97),
('Robert Lembke', 98),
('Winston Churchill', 99),
('Carl Friedrich von Weizsäcker', 100),
('Ephraim Kishon', 101),
('Plato', 102),
('Woody Allen', 103),
('Sir Peter Ustinov', 104),
('Maxim Gorki', 105),
('Salvador Dali', 106),
('Theodor Fontane', 107),
('Hermann Hesse', 108),
('Hägar der Schreckliche', 109),
('Urban Priol', 110),
('Deep Thought', 111),
('Jules Verne', 112),
('John Lennon', 113),
('Berti Vogts', 114),
('Rudi Völler', 115),
('Agatha Christie', 116),
('Brigitte Bardot', 117),
('Heinrich Böll', 118),
('Samuel Coleridge', 119),
('Bob Hope', 120),
('Robert Musil', 121),
('Loriot', 122),
('Ambrose Bierce', 123),
('Jürgen Wegmann', 124),
('Sepp Herberger', 125),
('Jean Paul Sartre', 126),
('Muhammad Ali', 127),
('Roland Wohlfarth', 128),
('Andreas Möller', 129),
('Gary Lineker', 130),
('Bruno Labbadia', 131),
('Giovanni Trapattoni', 132),
('Otto Rehhagel', 133),
('Elbert Hubbard', 134),
('Arthur Schopenhauer', 135),
('Gerhard Polt', 136),
('Irenäus Eibl-Eibesfeldt', 137);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
