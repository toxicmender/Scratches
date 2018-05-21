#!/usr/bin/perl
use strict;
use warnings;

# first, create your message
use Email::MIME;
my $message = Email::MIME->create(
  header_str => [
    From    => 'toxicmender@gmail.com',
    To      => 'danish.parvez19@gmail.com',
    Subject => 'Perl Test Mail!',
  ],
  attributes => {
    encoding => 'quoted-printable',
    charset  => 'ISO-8859-1',
  },
  body_str => "Body String!\n",
);

# send the message
use Email::Sender::Simple qw(sendmail);
sendmail($message);
