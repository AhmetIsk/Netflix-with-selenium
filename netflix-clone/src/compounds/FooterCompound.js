import React from "react";
import FooterWrapper from "../components/Footer/FooterWrapper";
import FooterTitle from "../components/Footer/FooterTitle";
import FooterRow from "../components/Footer/FooterRow";
import FooterColumn from "../components/Footer/FooterColumn";
import FooterLink from "../components/Footer/FooterLink";

function FooterCompound() {
  return (
    <FooterWrapper>
      <FooterTitle>Sorularınız mı var? 0850-390-7444 numaralı telefonu arayın</FooterTitle>
      <FooterRow>
        <FooterColumn>
          <FooterLink>SSS</FooterLink>
          <FooterLink>Çerez Tercihleri</FooterLink>
        </FooterColumn>
        <FooterColumn>
          <FooterLink>Yardım Merkezi</FooterLink>
          <FooterLink>Kurumsal Bilgiler</FooterLink>
        </FooterColumn>
        <FooterColumn>
          <FooterLink>Kullanım Koşulları</FooterLink>
        </FooterColumn>
        <FooterColumn>
          <FooterLink>Gizlilik</FooterLink>
        </FooterColumn>
      </FooterRow>
    </FooterWrapper>
  );
}

export default FooterCompound;
